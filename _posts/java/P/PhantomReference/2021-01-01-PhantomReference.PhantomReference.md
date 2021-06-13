---
title: PhantomReference.PhantomReference()
permalink: /Java/PhantomReference/PhantomReference/
date: 2021-01-11
key: Java.P.PhantomReference
category: java
tags: ['java se', 'java.lang.ref', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PhantomReference.constructores valor="PhantomReference" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PhantomReference(T referent, ReferenceQueue<? super T> q)
~~~

## Parámetros
* **ReferenceQueue&lt;? super T&gt; q**,  {% include w3api/param_description.html metodo=_dato parametro="ReferenceQueue<? super T> q" %}
* **T referent**,  {% include w3api/param_description.html metodo=_dato parametro="T referent" %}

## Clase Padre
[PhantomReference](/Java/PhantomReference/)

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
