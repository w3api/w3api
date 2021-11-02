---
title: gettext.NullTranslations.npgettext
permalink: /Python/gettext/NullTranslations/npgettext/
date: 2021-01-01
key: Python.G.gettext.NullTranslations.npgettext
category: python
tags: ['metodo python', 'gettext']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.G.gettext.NullTranslations.metodos valor="npgettext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~python
{{ _dato.sintaxis }}~~~

## Parámetros
* **context**,  {% include w3api/function_param_description.html propiedad=_dato valor="context" %}
* **n**,  {% include w3api/function_param_description.html propiedad=_dato valor="n" %}
* **plural**,  {% include w3api/function_param_description.html propiedad=_dato valor="plural" %}
* **singular**,  {% include w3api/function_param_description.html propiedad=_dato valor="singular" %}

## Clase Padre
[NullTranslations](/Python/gettext/NullTranslations/)

## Ejemplo
~~~python
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
