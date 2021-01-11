---
title: KerberosTicket.KerberosTicket()
permalink: Java/KerberosTicket/KerberosTicket
date: 2021-01-11
key: JavaJava.K.KerberosTicket
category: java
tags: ['java se', 'javax.security.auth.kerberos', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KerberosTicket.constructores valor="KerberosTicket" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public KerberosTicket(byte[] asn1Encoding, KerberosPrincipal client, KerberosPrincipal server, byte[] sessionKey, int keyType, boolean[] flags, Date authTime, Date startTime, Date endTime, Date renewTill, InetAddress[] clientAddresses)
~~~

## Parámetros
* **KerberosPrincipal server**,  {% include w3api/param_description.html metodo=_dato parametro="KerberosPrincipal server" %}
* **Date endTime**,  {% include w3api/param_description.html metodo=_dato parametro="Date endTime" %}
* **byte[] asn1Encoding**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] asn1Encoding" %}
* **KerberosPrincipal client**,  {% include w3api/param_description.html metodo=_dato parametro="KerberosPrincipal client" %}
* **byte[] sessionKey**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] sessionKey" %}
* **Date renewTill**,  {% include w3api/param_description.html metodo=_dato parametro="Date renewTill" %}
* **InetAddress[] clientAddresses**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress[] clientAddresses" %}
* **int keyType**,  {% include w3api/param_description.html metodo=_dato parametro="int keyType" %}
* **boolean[] flags**,  {% include w3api/param_description.html metodo=_dato parametro="boolean[] flags" %}
* **Date startTime**,  {% include w3api/param_description.html metodo=_dato parametro="Date startTime" %}
* **Date authTime**,  {% include w3api/param_description.html metodo=_dato parametro="Date authTime" %}

## Clase Padre
[KerberosTicket](/Java/KerberosTicket/)

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
