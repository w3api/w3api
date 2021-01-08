---
title: KeySelector.select()
permalink: Java/KeySelector/select
date: 2021-01-04
key: JavaJava.K.KeySelector
category: java
tags: ['java se', 'javax.xml.crypto', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeySelector.metodos valor="select" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract KeySelectorResult select(KeyInfo keyInfo, KeySelector.Purpose purpose, AlgorithmMethod method, XMLCryptoContext context) throws KeySelectorException
~~~

## Parámetros
* **AlgorithmMethod method**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmMethod method" %}
* **KeySelector.Purpose purpose**,  {% include w3api/param_description.html metodo=_data parametro="KeySelector.Purpose purpose" %}
* **KeyInfo keyInfo**,  {% include w3api/param_description.html metodo=_data parametro="KeyInfo keyInfo" %}
* **XMLCryptoContext context**,  {% include w3api/param_description.html metodo=_data parametro="XMLCryptoContext context" %}

## Excepciones
[KeySelectorException](/Java/KeySelectorException/), [ClassCastException](/Java/ClassCastException/)

## Clase Padre
[KeySelector](/Java/KeySelector/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeySelector.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
