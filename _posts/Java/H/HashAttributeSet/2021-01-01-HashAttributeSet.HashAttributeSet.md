---
title: HashAttributeSet.HashAttributeSet()
permalink: /Java/HashAttributeSet/HashAttributeSet/
date: 2021-01-11
key: Java.H.HashAttributeSet
category: Java
tags: ['java se', 'javax.print.attribute', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HashAttributeSet.constructores valor="HashAttributeSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public HashAttributeSet()
protected HashAttributeSet(Class<?> interfaceName)
public HashAttributeSet(Attribute attribute)
public HashAttributeSet(Attribute[] attributes)
protected HashAttributeSet(Attribute[] attributes, Class<?> interfaceName)
protected HashAttributeSet(Attribute attribute, Class<?> interfaceName)
public HashAttributeSet(AttributeSet attributes)
protected HashAttributeSet(AttributeSet attributes, Class<?> interfaceName)
~~~

## Parámetros
* **Attribute attribute**,  {% include w3api/param_description.html metodo=_dato parametro="Attribute attribute" %}
* **Class&lt;?&gt; interfaceName**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> interfaceName" %}
* **Attribute[] attributes**,  {% include w3api/param_description.html metodo=_dato parametro="Attribute[] attributes" %}
* **AttributeSet attributes**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attributes" %}

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
