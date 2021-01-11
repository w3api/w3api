---
title: KeyInfoFactory.newKeyInfo()
permalink: Java/KeyInfoFactory/newKeyInfo
date: 2021-01-11
key: JavaJava.K.KeyInfoFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig.keyinfo', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyInfoFactory.metodos valor="newKeyInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract KeyInfo newKeyInfo(List<? extends XMLStructure> content)
public abstract KeyInfo newKeyInfo(List<? extends XMLStructure> content, String id)
~~~

## Parámetros
* **String id**,  {% include w3api/param_description.html metodo=_dato parametro="String id" %}
* **List&lt;? extends XMLStructure&gt; content**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends XMLStructure> content" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[KeyInfoFactory](/Java/KeyInfoFactory/)

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
