---
title: ObjectOutputStream.writeClassDescriptor()
permalink: Java/ObjectOutputStream/writeClassDescriptor
date: 2021-01-11
key: JavaJava.O.ObjectOutputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectOutputStream.metodos valor="writeClassDescriptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void writeClassDescriptor(ObjectStreamClass desc) throws IOException
~~~

## Parámetros
* **ObjectStreamClass desc**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectStreamClass desc" %}

## Excepciones
[IOException](/Java/IOException/)

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
