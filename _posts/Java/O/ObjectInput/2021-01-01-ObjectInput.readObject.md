---
title: ObjectInput.readObject()
permalink: /Java/ObjectInput/readObject/
date: 2021-01-11
key: Java.O.ObjectInput
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectInput.metodos valor="readObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object readObject() throws ClassNotFoundException, IOException
~~~

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[ObjectInput](/Java/ObjectInput/)

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
