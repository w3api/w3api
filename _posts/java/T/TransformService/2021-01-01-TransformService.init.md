---
title: TransformService.init()
permalink: Java/TransformService/init
date: 2021-01-11
key: JavaJava.T.TransformService
category: java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransformService.metodos valor="init" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void init(TransformParameterSpec params) throws InvalidAlgorithmParameterException
public abstract void init(XMLStructure parent, XMLCryptoContext context) throws InvalidAlgorithmParameterException
~~~

## Parámetros
* **XMLStructure parent**,  {% include w3api/param_description.html metodo=_dato parametro="XMLStructure parent" %}
* **XMLCryptoContext context**,  {% include w3api/param_description.html metodo=_dato parametro="XMLCryptoContext context" %}
* **TransformParameterSpec params**,  {% include w3api/param_description.html metodo=_dato parametro="TransformParameterSpec params" %}

## Excepciones
[InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[TransformService](/Java/TransformService/)

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
