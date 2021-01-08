---
title: ServicePermission.ServicePermission()
permalink: Java/ServicePermission/ServicePermission
date: 2021-01-04
key: JavaJava.S.ServicePermission
category: java
tags: ['java se', 'javax.security.auth.kerberos', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServicePermission.constructores valor="ServicePermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ServicePermission(String servicePrincipal, String action)
~~~

## Parámetros
* **String action**,  {% include w3api/param_description.html metodo=_data parametro="String action" %}
* **String servicePrincipal**,  {% include w3api/param_description.html metodo=_data parametro="String servicePrincipal" %}

## Clase Padre
[ServicePermission](/Java/ServicePermission/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ServicePermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
