---
title: LinkerServices.canConvert()
permalink: /Java/LinkerServices/canConvert/
date: 2021-01-11
key: Java.L.LinkerServices
category: Java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkerServices.metodos valor="canConvert" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean canConvert(Class<?> from, Class<?> to)
~~~

## Parámetros
* **Class&lt;?&gt; to**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> to" %}
* **Class&lt;?&gt; from**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> from" %}

## Clase Padre
[LinkerServices](/Java/LinkerServices/)

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
