---
title: PKIXParameters.setTrustAnchors()
permalink: /Java/PKIXParameters/setTrustAnchors/
date: 2021-01-11
key: Java.P.PKIXParameters
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PKIXParameters.metodos valor="setTrustAnchors" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setTrustAnchors(Set<TrustAnchor> trustAnchors) throws InvalidAlgorithmParameterException
~~~

## Parámetros
* **Set&lt;TrustAnchor&gt; trustAnchors**,  {% include w3api/param_description.html metodo=_dato parametro="Set<TrustAnchor> trustAnchors" %}

## Excepciones
[InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PKIXParameters](/Java/PKIXParameters/)

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
