---
title: ValueDescriptor.getAnnotation()
permalink: /Java/ValueDescriptor/getAnnotation/
date: 2021-01-11
key: Java.V.ValueDescriptor
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.ValueDescriptor.metodos valor="getAnnotation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<A extends Annotation>A getAnnotation(Class<A> annotationType)
~~~

## Parámetros
* **Class&lt;A&gt; annotationType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<A> annotationType" %}

## Clase Padre
[ValueDescriptor](/Java/ValueDescriptor/)

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
