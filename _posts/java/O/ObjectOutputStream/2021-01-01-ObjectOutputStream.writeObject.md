---
title: ObjectOutputStream.writeObject()
permalink: /Java/ObjectOutputStream/writeObject/
date: 2021-01-11
key: Java.O.ObjectOutputStream
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectOutputStream.metodos valor="writeObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void writeObject(Object obj) throws IOException
~~~

## Parámetros
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}

## Excepciones
[InvalidClassException](/Java/InvalidClassException/), [NotSerializableException](/Java/NotSerializableException/), [IOException](/Java/IOException/)

## Clase Padre
[ObjectOutputStream](/Java/ObjectOutputStream/)

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
