---
title: SoftReference.SoftReference()
permalink: /Java/SoftReference/SoftReference/
date: 2021-01-11
key: Java.S.SoftReference
category: Java
tags: ['java se', 'java.lang.ref', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SoftReference.constructores valor="SoftReference" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SoftReference(T referent)
public SoftReference(T referent, ReferenceQueue<? super T> q)
~~~

## Parámetros
* **ReferenceQueue&lt;? super T&gt; q**,  {% include w3api/param_description.html metodo=_dato parametro="ReferenceQueue<? super T> q" %}
* **T referent**,  {% include w3api/param_description.html metodo=_dato parametro="T referent" %}

## Clase Padre
[SoftReference](/Java/SoftReference/)

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
