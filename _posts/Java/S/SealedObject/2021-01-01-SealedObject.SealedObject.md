---
title: SealedObject.SealedObject()
permalink: /Java/SealedObject/SealedObject/
date: 2021-01-11
key: Java.S.SealedObject
category: Java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SealedObject.constructores valor="SealedObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SealedObject(Serializable object, Cipher c) throws IOException, IllegalBlockSizeException
protected SealedObject(SealedObject so)
~~~

## Parámetros
* **Cipher c**,  {% include w3api/param_description.html metodo=_dato parametro="Cipher c" %}
* **SealedObject so**,  {% include w3api/param_description.html metodo=_dato parametro="SealedObject so" %}
* **Serializable object**,  {% include w3api/param_description.html metodo=_dato parametro="Serializable object" %}

## Excepciones
[IllegalBlockSizeException](/Java/IllegalBlockSizeException/), [IOException](/Java/IOException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SealedObject](/Java/SealedObject/)

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
