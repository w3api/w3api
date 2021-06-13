---
title: KeyInfoFactory.newRetrievalMethod()
permalink: /Java/KeyInfoFactory/newRetrievalMethod/
date: 2021-01-11
key: Java.K.KeyInfoFactory
category: Java
tags: ['java se', 'javax.xml.crypto.dsig.keyinfo', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyInfoFactory.metodos valor="newRetrievalMethod" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract RetrievalMethod newRetrievalMethod(String uri)
public abstract RetrievalMethod newRetrievalMethod(String uri, String type, List<? extends Transform> transforms)
~~~

## Parámetros
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **List&lt;? extends Transform&gt; transforms**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends Transform> transforms" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}

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
