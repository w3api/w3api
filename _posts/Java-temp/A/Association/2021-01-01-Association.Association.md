---
title: Association.Association()
permalink: /Java/Association/Association/
date: 2021-01-11
key: Java.A.Association
category: Java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Association.constructores valor="Association" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Association(int associationID, int maxInStreams, int maxOutStreams)
~~~

## Parámetros
* **int associationID**,  {% include w3api/param_description.html metodo=_dato parametro="int associationID" %}
* **int maxInStreams**,  {% include w3api/param_description.html metodo=_dato parametro="int maxInStreams" %}
* **int maxOutStreams**,  {% include w3api/param_description.html metodo=_dato parametro="int maxOutStreams" %}

## Clase Padre
[Association](/Java/Association/)

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
