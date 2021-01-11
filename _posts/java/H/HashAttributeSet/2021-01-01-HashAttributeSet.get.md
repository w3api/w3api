---
title: HashAttributeSet.get()
permalink: Java/HashAttributeSet/get
date: 2021-01-11
key: JavaJava.H.HashAttributeSet
category: java
tags: ['java se', 'javax.print.attribute', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HashAttributeSet.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Attribute get(Class<?> category)
~~~

## Parámetros
* **Class&lt;?&gt; category**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> category" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[HashAttributeSet](/Java/HashAttributeSet/)

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
