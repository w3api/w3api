---
title: SimpleType.readResolve()
permalink: Java/SimpleType/readResolve
date: 2021-01-04
key: JavaJava.S.SimpleType
category: java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleType.metodos valor="readResolve" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object readResolve() throws ObjectStreamException
~~~

## Excepciones
[ObjectStreamException](/Java/ObjectStreamException/)

## Clase Padre
[SimpleType](/Java/SimpleType/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleType.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
