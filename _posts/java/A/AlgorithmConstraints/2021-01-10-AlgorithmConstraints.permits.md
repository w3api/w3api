---
title: AlgorithmConstraints.permits()
permalink: Java/AlgorithmConstraints/permits
date: 2021-01-10
key: JavaJava.A.AlgorithmConstraints
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AlgorithmConstraints.metodos valor="permits" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean permits(Set<CryptoPrimitive> primitives, String algorithm, AlgorithmParameters parameters)
boolean permits(Set<CryptoPrimitive> primitives, String algorithm, Key key, AlgorithmParameters parameters)
boolean permits(Set<CryptoPrimitive> primitives, Key key)
~~~

## Parámetros
* **Set&lt;CryptoPrimitive&gt; primitives**,  {% include w3api/param_description.html metodo=_dato parametro="Set<CryptoPrimitive> primitives" %}
* **AlgorithmParameters parameters**,  {% include w3api/param_description.html metodo=_dato parametro="AlgorithmParameters parameters" %}
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}
* **Key key**,  {% include w3api/param_description.html metodo=_dato parametro="Key key" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AlgorithmConstraints](/Java/AlgorithmConstraints/)

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
