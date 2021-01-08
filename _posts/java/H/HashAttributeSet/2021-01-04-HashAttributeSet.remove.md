---
title: HashAttributeSet.remove()
permalink: Java/HashAttributeSet/remove
date: 2021-01-04
key: JavaJava.H.HashAttributeSet
category: java
tags: ['java se', 'javax.print.attribute', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HashAttributeSet.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean remove(Class<?> category)
public boolean remove(Attribute attribute)
~~~

## Parámetros
* **Attribute attribute**,  {% include w3api/param_description.html metodo=_data parametro="Attribute attribute" %}
* **Class&lt;?&gt; category**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> category" %}

## Excepciones
[UnmodifiableSetException](/Java/UnmodifiableSetException/)

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
