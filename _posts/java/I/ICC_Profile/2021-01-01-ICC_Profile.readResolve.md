---
title: ICC_Profile.readResolve()
permalink: /Java/ICC_Profile/readResolve/
date: 2021-01-11
key: Java.I.ICC_Profile
category: Java
tags: ['java se', 'java.awt.color', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ICC_Profile.metodos valor="readResolve" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Object readResolve() throws ObjectStreamException
~~~

## Excepciones
[ObjectStreamException](/Java/ObjectStreamException/)

## Clase Padre
[ICC_Profile](/Java/ICC_Profile/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
