export interface Route {
  path: string;
  name: string;
  section: 'attraction' | 'corporate' | 'meta';
}

export const ROUTES: Route[] = [
  // Attraction side
  { path: '/',                     name: 'home',               section: 'attraction' },
  { path: '/attraction',           name: 'attraction',         section: 'attraction' },
  { path: '/arcade',               name: 'arcade',             section: 'attraction' },
  { path: '/museum',               name: 'museum',             section: 'attraction' },
  { path: '/workshop',             name: 'workshop',           section: 'attraction' },
  { path: '/fortune',              name: 'fortune',            section: 'attraction' },
  { path: '/gift-shop',            name: 'gift-shop',          section: 'attraction' },
  { path: '/crossroads',           name: 'crossroads',         section: 'attraction' },
  { path: '/chapel',               name: 'chapel',             section: 'attraction' },
  { path: '/chapel/back-room',     name: 'chapel-back-room',   section: 'attraction' },
  { path: '/cathedral',            name: 'cathedral',          section: 'attraction' },
  { path: '/deep-garden',          name: 'deep-garden',        section: 'attraction' },
  { path: '/employees-only',       name: 'employees-only',     section: 'attraction' },
  // Corporate / studio side
  { path: '/work',                 name: 'work',               section: 'corporate' },
  { path: '/work/intake',          name: 'work-intake',        section: 'corporate' },
  { path: '/work/case-files',      name: 'work-case-files',    section: 'corporate' },
  { path: '/studio',               name: 'studio',             section: 'corporate' },
  { path: '/studio/field-notes',   name: 'studio-field-notes', section: 'corporate' },
  { path: '/studio/infrastructure',name: 'studio-infrastructure', section: 'corporate' },
  // Meta
  { path: '/about',                name: 'about',              section: 'meta' },
];
