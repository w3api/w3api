---
title: EnumSyntax.readResolve()
permalink: Java/EnumSyntax/readResolve
date: 2021-01-11
key: JavaJava.E.EnumSyntax
category: java
tags: ['java se', 'javax.print.attribute', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EnumSyntax.metodos valor="readResolve" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Object readResolve() throws ObjectStreamException
~~~

## Excepciones
[InvalidObjectException](/Java/InvalidObjectException/), [ObjectStreamException](/Java/ObjectStreamException/)

## Clase Padre
[EnumSyntax](/Java/EnumSyntax/)

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