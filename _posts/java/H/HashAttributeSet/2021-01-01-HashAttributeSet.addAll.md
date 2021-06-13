---
title: HashAttributeSet.addAll()
permalink: /Java/HashAttributeSet/addAll/
date: 2021-01-11
key: Java.H.HashAttributeSet
category: Java
tags: ['java se', 'javax.print.attribute', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HashAttributeSet.metodos valor="addAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean addAll(AttributeSet attributes)
~~~

## Parámetros
* **AttributeSet attributes**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attributes" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [UnmodifiableSetException](/Java/UnmodifiableSetException/)

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
