---
title: HashAttributeSet.add()
permalink: Java/HashAttributeSet/add
date: 2021-01-11
key: JavaJava.H.HashAttributeSet
category: java
tags: ['java se', 'javax.print.attribute', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HashAttributeSet.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean add(Attribute attribute)
~~~

## Parámetros
* **Attribute attribute**,  {% include w3api/param_description.html metodo=_dato parametro="Attribute attribute" %}

## Excepciones
[UnmodifiableSetException](/Java/UnmodifiableSetException/), [NullPointerException](/Java/NullPointerException/)

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
