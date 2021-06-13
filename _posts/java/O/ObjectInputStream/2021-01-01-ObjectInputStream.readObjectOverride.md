---
title: ObjectInputStream.readObjectOverride()
permalink: /Java/ObjectInputStream/readObjectOverride/
date: 2021-01-11
key: JavaJava.O.ObjectInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectInputStream.metodos valor="readObjectOverride" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Object readObjectOverride() throws IOException, ClassNotFoundException
~~~

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [OptionalDataException](/Java/OptionalDataException/), [IOException](/Java/IOException/)

## Clase Padre
[ObjectInputStream](/Java/ObjectInputStream/)

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
