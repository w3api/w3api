---
title: HashAttributeSet.HashAttributeSet()
permalink: Java/HashAttributeSet/HashAttributeSet
date: 2021-01-04
key: JavaJava.H.HashAttributeSet
category: java
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
* **Attribute[] attributes**,  {% include w3api/param_description.html metodo=_data parametro="Attribute[] attributes" %}
* **AttributeSet attributes**,  {% include w3api/param_description.html metodo=_data parametro="AttributeSet attributes" %}
* **Class&lt;?&gt; interfaceName**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> interfaceName" %}
* **Attribute attribute**,  {% include w3api/param_description.html metodo=_data parametro="Attribute attribute" %}

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
{%- for _ldc in site.data.Java.H.HashAttributeSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
