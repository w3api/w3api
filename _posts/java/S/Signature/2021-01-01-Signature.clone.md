---
title: Signature.clone()
permalink: /Java/Signature/clone/
date: 2021-01-11
key: Java.S.Signature
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Signature.metodos valor="clone" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object clone() throws CloneNotSupportedException
~~~

## Excepciones
[CloneNotSupportedException](/Java/CloneNotSupportedException/)

## Clase Padre
[Signature](/Java/Signature/)

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
