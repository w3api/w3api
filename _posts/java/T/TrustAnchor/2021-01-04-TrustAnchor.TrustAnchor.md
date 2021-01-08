---
title: TrustAnchor.TrustAnchor()
permalink: Java/TrustAnchor/TrustAnchor
date: 2021-01-04
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
* **X509Certificate trustedCert**,  {% include w3api/param_description.html metodo=_data parametro="X509Certificate trustedCert" %}
* **String caName**,  {% include w3api/param_description.html metodo=_data parametro="String caName" %}
* **PublicKey pubKey**,  {% include w3api/param_description.html metodo=_data parametro="PublicKey pubKey" %}
* **byte[] nameConstraints**,  {% include w3api/param_description.html metodo=_data parametro="byte[] nameConstraints" %}
* **X500Principal caPrincipal**,  {% include w3api/param_description.html metodo=_data parametro="X500Principal caPrincipal" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[TrustAnchor](/Java/TrustAnchor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TrustAnchor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
