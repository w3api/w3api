---
title: ObjectInputStream.GetField.defaulted()
permalink: Java/ObjectInputStream/GetField/defaulted
date: 2021-01-11
key: JavaJava.O.ObjectInputStream.GetField
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectInputStream.GetField.metodos valor="defaulted" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean defaulted(String name) throws IOException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[ObjectInputStream.GetField](/Java/ObjectInputStream/GetField/)

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
