---
title: Chronology.getDisplayName()
permalink: /Java/Chronology/getDisplayName/
date: 2021-01-11
key: Java.C.Chronology
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Chronology.metodos valor="getDisplayName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default String getDisplayName(TextStyle style, Locale locale)
~~~

## Parámetros
* **TextStyle style**,  {% include w3api/param_description.html metodo=_dato parametro="TextStyle style" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Clase Padre
[Chronology](/Java/Chronology/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
