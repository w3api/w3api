---
title: SignedObject.getObject()
permalink: /Java/SignedObject/getObject/
date: 2021-01-11
key: Java.S.SignedObject
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SignedObject.metodos valor="getObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getObject() throws IOException, ClassNotFoundException
~~~

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[SignedObject](/Java/SignedObject/)

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
