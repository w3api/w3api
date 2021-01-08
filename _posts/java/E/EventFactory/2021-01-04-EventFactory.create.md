---
title: EventFactory.create()
permalink: Java/EventFactory/create
date: 2021-01-04
key: JavaJava.E.EventFactory
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventFactory.metodos valor="create" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static EventFactory create(List<AnnotationElement> annotationElements, List<ValueDescriptor> fields)
~~~

## Parámetros
* **List&lt;AnnotationElement&gt; annotationElements**,  {% include w3api/param_description.html metodo=_data parametro="List<AnnotationElement> annotationElements" %}
* **List&lt;ValueDescriptor&gt; fields**,  {% include w3api/param_description.html metodo=_data parametro="List<ValueDescriptor> fields" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[EventFactory](/Java/EventFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EventFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
