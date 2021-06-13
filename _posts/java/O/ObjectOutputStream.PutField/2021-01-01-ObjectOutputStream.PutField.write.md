---
title: ObjectOutputStream.PutField.write()
permalink: /Java/ObjectOutputStream/PutField/write/
date: 2021-01-11
key: JavaJava.O.ObjectOutputStream.PutField
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectOutputStream.PutField.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public abstract void write(ObjectOutput out) throws IOException
~~~

## Parámetros
* **ObjectOutput out**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectOutput out" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[ObjectOutputStream.PutField](/Java/ObjectOutputStream/PutField/)

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
