---
title: ClassDefinition.ClassDefinition()
permalink: Java/ClassDefinition/ClassDefinition
date: 2021-01-04
key: JavaJava.C.ClassDefinition
category: java
tags: ['java se', 'java.lang.instrument', 'java.instrument', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassDefinition.constructores valor="ClassDefinition" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ClassDefinition(Class<?> theClass, byte[] theClassFile)
~~~

## Parámetros
* **Class&lt;?&gt; theClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> theClass" %}
* **byte[] theClassFile**,  {% include w3api/param_description.html metodo=_data parametro="byte[] theClassFile" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ClassDefinition](/Java/ClassDefinition/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClassDefinition.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
