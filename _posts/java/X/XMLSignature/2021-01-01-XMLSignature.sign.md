---
title: XMLSignature.sign()
permalink: Java/XMLSignature/sign
date: 2021-01-11
key: JavaJava.X.XMLSignature
category: java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLSignature.metodos valor="sign" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void sign(XMLSignContext signContext) throws MarshalException, XMLSignatureException
~~~

## Parámetros
* **XMLSignContext signContext**,  {% include w3api/param_description.html metodo=_dato parametro="XMLSignContext signContext" %}

## Excepciones
[MarshalException](/Java/MarshalException/), [ClassCastException](/Java/ClassCastException/), [XMLSignatureException](/Java/XMLSignatureException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[XMLSignature](/Java/XMLSignature/)

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
