---
title: IncompleteAnnotationException.IncompleteAnnotationException()
permalink: Java/IncompleteAnnotationException/IncompleteAnnotationException
date: 2021-01-04
key: JavaJava.I.IncompleteAnnotationException
category: java
tags: ['java se', 'java.lang.annotation', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IncompleteAnnotationException.constructores valor="IncompleteAnnotationException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IncompleteAnnotationException(Class<? extends Annotation> annotationType, String elementName)
~~~

## Parámetros
* **String elementName**,  {% include w3api/param_description.html metodo=_data parametro="String elementName" %}
* **Class&lt;? extends Annotation&gt; annotationType**,  {% include w3api/param_description.html metodo=_data parametro="Class<? extends Annotation> annotationType" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[IncompleteAnnotationException](/Java/IncompleteAnnotationException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IncompleteAnnotationException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
