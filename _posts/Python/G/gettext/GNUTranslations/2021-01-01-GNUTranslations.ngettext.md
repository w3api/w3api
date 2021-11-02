---
title: gettext.GNUTranslations.ngettext
permalink: /Python/gettext/GNUTranslations/ngettext/
date: 2021-01-01
key: Python.G.gettext.GNUTranslations.ngettext
category: python
tags: ['metodo python', 'gettext']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.G.gettext.GNUTranslations.metodos valor="ngettext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~python
{{ _dato.sintaxis }}~~~

## Parámetros
* **n**,  {% include w3api/function_param_description.html propiedad=_dato valor="n" %}
* **plural**,  {% include w3api/function_param_description.html propiedad=_dato valor="plural" %}
* **singular**,  {% include w3api/function_param_description.html propiedad=_dato valor="singular" %}

## Clase Padre
[GNUTranslations](/Python/gettext/GNUTranslations/)

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
