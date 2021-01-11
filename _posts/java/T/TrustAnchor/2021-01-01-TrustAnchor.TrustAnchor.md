---
title: TrustAnchor.TrustAnchor()
permalink: Java/TrustAnchor/TrustAnchor
date: 2021-01-11
key: JavaJava.T.TrustAnchor
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TrustAnchor.constructores valor="TrustAnchor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TrustAnchor(String caName, PublicKey pubKey, byte[] nameConstraints)
public TrustAnchor(X509Certificate trustedCert, byte[] nameConstraints)
public TrustAnchor(X500Principal caPrincipal, PublicKey pubKey, byte[] nameConstraints)
~~~

## Parámetros
* **X500Principal caPrincipal**,  {% include w3api/param_description.html metodo=_dato parametro="X500Principal caPrincipal" %}
* **PublicKey pubKey**,  {% include w3api/param_description.html metodo=_dato parametro="PublicKey pubKey" %}
* **String caName**,  {% include w3api/param_description.html metodo=_dato parametro="String caName" %}
* **byte[] nameConstraints**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] nameConstraints" %}
* **X509Certificate trustedCert**,  {% include w3api/param_description.html metodo=_dato parametro="X509Certificate trustedCert" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[TrustAnchor](/Java/TrustAnchor/)

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
