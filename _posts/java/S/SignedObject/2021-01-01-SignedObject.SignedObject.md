---
title: SignedObject.SignedObject()
permalink: /Java/SignedObject/SignedObject/
date: 2021-01-11
key: Java.S.SignedObject
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SignedObject.constructores valor="SignedObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SignedObject(Serializable object, PrivateKey signingKey, Signature signingEngine) throws IOException, InvalidKeyException, SignatureException
~~~

## Parámetros
* **PrivateKey signingKey**,  {% include w3api/param_description.html metodo=_dato parametro="PrivateKey signingKey" %}
* **Signature signingEngine**,  {% include w3api/param_description.html metodo=_dato parametro="Signature signingEngine" %}
* **Serializable object**,  {% include w3api/param_description.html metodo=_dato parametro="Serializable object" %}

## Excepciones
[SignatureException](/Java/SignatureException/), [InvalidKeyException](/Java/InvalidKeyException/), [IOException](/Java/IOException/)

## Clase Padre
[SignedObject](/Java/SignedObject/)

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
