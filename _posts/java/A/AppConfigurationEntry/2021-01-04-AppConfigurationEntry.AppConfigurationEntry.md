---
title: AppConfigurationEntry.AppConfigurationEntry()
permalink: Java/AppConfigurationEntry/AppConfigurationEntry
date: 2021-01-04
key: JavaJava.A.AppConfigurationEntry
category: java
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
* **AppConfigurationEntry.LoginModuleControlFlag controlFlag**,  {% include w3api/param_description.html metodo=_data parametro="AppConfigurationEntry.LoginModuleControlFlag controlFlag" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **String loginModuleName**,  {% include w3api/param_description.html metodo=_data parametro="String loginModuleName" %}
* **?&gt; options**,  {% include w3api/param_description.html metodo=_data parametro="?> options" %}

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
{%- for _ldc in site.data.Java.A.AppConfigurationEntry.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
