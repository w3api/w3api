---
title: TransformService.marshalParams()
permalink: /Java/TransformService/marshalParams/
date: 2021-01-11
key: Java.T.TransformService
category: Java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransformService.metodos valor="marshalParams" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void marshalParams(XMLStructure parent, XMLCryptoContext context) throws MarshalException
~~~

## Parámetros
* **XMLStructure parent**,  {% include w3api/param_description.html metodo=_dato parametro="XMLStructure parent" %}
* **XMLCryptoContext context**,  {% include w3api/param_description.html metodo=_dato parametro="XMLCryptoContext context" %}

## Excepciones
[MarshalException](/Java/MarshalException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

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
