---
title: ValueDescriptor.ValueDescriptor()
permalink: Java/ValueDescriptor/ValueDescriptor
date: 2021-01-11
key: JavaJava.V.ValueDescriptor
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.ValueDescriptor.constructores valor="ValueDescriptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ValueDescriptor(Class<?> type, String name)
public ValueDescriptor(Class<?> type, String name, List<AnnotationElement> annotations)
~~~

## Parámetros
* **Class&lt;?&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> type" %}
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **List&lt;AnnotationElement&gt; annotations**,  {% include w3api/param_description.html metodo=_dato parametro="List<AnnotationElement> annotations" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

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
