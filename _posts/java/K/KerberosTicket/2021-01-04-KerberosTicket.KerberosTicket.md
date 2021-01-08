---
title: KerberosTicket.KerberosTicket()
permalink: Java/KerberosTicket/KerberosTicket
date: 2021-01-04
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
* **Date authTime**,  {% include w3api/param_description.html metodo=_data parametro="Date authTime" %}
* **Date startTime**,  {% include w3api/param_description.html metodo=_data parametro="Date startTime" %}
* **InetAddress[] clientAddresses**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress[] clientAddresses" %}
* **KerberosPrincipal client**,  {% include w3api/param_description.html metodo=_data parametro="KerberosPrincipal client" %}
* **boolean[] flags**,  {% include w3api/param_description.html metodo=_data parametro="boolean[] flags" %}
* **int keyType**,  {% include w3api/param_description.html metodo=_data parametro="int keyType" %}
* **Date renewTill**,  {% include w3api/param_description.html metodo=_data parametro="Date renewTill" %}
* **KerberosPrincipal server**,  {% include w3api/param_description.html metodo=_data parametro="KerberosPrincipal server" %}
* **Date endTime**,  {% include w3api/param_description.html metodo=_data parametro="Date endTime" %}
* **byte[] asn1Encoding**,  {% include w3api/param_description.html metodo=_data parametro="byte[] asn1Encoding" %}
* **byte[] sessionKey**,  {% include w3api/param_description.html metodo=_data parametro="byte[] sessionKey" %}

## Clase Padre
[KerberosTicket](/Java/KerberosTicket/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KerberosTicket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
