---
title: MarshalledObject.get()
permalink: Java/MarshalledObject/get
date: 2021-01-04
key: JavaJava.M.MarshalledObject
category: java
tags: ['java se', 'java.rmi', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MarshalledObject.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public T get() throws IOException, ClassNotFoundException
~~~

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[MarshalledObject](/Java/MarshalledObject/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MarshalledObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
