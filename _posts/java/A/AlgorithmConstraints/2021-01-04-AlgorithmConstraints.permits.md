---
title: AlgorithmConstraints.permits()
permalink: Java/AlgorithmConstraints/permits
date: 2021-01-04
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
* **String algorithm**,  {% include w3api/param_description.html metodo=_data parametro="String algorithm" %}
* **AlgorithmParameters parameters**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameters parameters" %}
* **Set&lt;CryptoPrimitive&gt; primitives**,  {% include w3api/param_description.html metodo=_data parametro="Set<CryptoPrimitive> primitives" %}
* **Key key**,  {% include w3api/param_description.html metodo=_data parametro="Key key" %}

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
{%- for _ldc in site.data.Java.A.AlgorithmConstraints.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
