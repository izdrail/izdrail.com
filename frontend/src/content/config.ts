import { defineCollection, z } from 'astro:content';

export const collections = {

	work: defineCollection({
		schema: z.object({
			title: z.string(),
			description: z.string(),
			publishDate: z.coerce.date(),
			tags: z.array(z.string()),
            image: z.string(),
		}),
	}),

    services: defineCollection({
        schema: z.object({
            title: z.string(),
            image: z.string(),
            tags: z.array(z.string()),
            description: z.string(),
            publishDate: z.coerce.date(),
        }),
    }),

    books: defineCollection({
        schema: z.object({
            title: z.string(),
            tags: z.array(z.string()),
            description: z.string(),
            img: z.string(),
        }),
    }),

    cheatsheets: defineCollection({
        schema: z.object({
            title: z.string(),
            tags: z.array(z.string()),
            description: z.string(),
        }),
    }),
    magazines: defineCollection({
        schema: z.object({
            title: z.string(),
            tags: z.array(z.string()),
            description: z.string(),
        }),
    }),


    blog: defineCollection({
        schema: z.object({
            title: z.string(),
            img: z.string(),
            description: z.string(),
            tags: z.array(z.string()),
        }),
    }),
};
