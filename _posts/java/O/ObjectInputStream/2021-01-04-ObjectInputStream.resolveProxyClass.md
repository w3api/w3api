---
title: ObjectInputStream.resolveProxyClass()
permalink: Java/ObjectInputStream/resolveProxyClass
date: 2021-01-04
key: JavaJava.O.ObjectInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectInputStream.metodos valor="resolveProxyClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Class<?> resolveProxyClass(String[] interfaces) throws IOException, ClassNotFoundException
~~~

## Parámetros
* **String[] interfaces**,  {% include w3api/param_description.html metodo=_data parametro="String[] interfaces" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[ObjectInputStream](/Java/ObjectInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
