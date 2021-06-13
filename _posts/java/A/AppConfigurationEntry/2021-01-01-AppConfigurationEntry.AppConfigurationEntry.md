---
title: AppConfigurationEntry.AppConfigurationEntry()
permalink: /Java/AppConfigurationEntry/AppConfigurationEntry/
date: 2021-01-11
key: Java.A.AppConfigurationEntry
category: Java
tags: ['java se', 'javax.security.auth.login', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AppConfigurationEntry.constructores valor="AppConfigurationEntry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AppConfigurationEntry(String loginModuleName, AppConfigurationEntry.LoginModuleControlFlag controlFlag, Map<String,?> options)
~~~

## Parámetros
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **String loginModuleName**,  {% include w3api/param_description.html metodo=_dato parametro="String loginModuleName" %}
* **?&gt; options**,  {% include w3api/param_description.html metodo=_dato parametro="?> options" %}
* **AppConfigurationEntry.LoginModuleControlFlag controlFlag**,  {% include w3api/param_description.html metodo=_dato parametro="AppConfigurationEntry.LoginModuleControlFlag controlFlag" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AppConfigurationEntry](/Java/AppConfigurationEntry/)

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
