---
title: ConfigurationSpi.engineGetAppConfigurationEntry()
permalink: Java/ConfigurationSpi/engineGetAppConfigurationEntry
date: 2021-01-04
key: JavaJava.C.ConfigurationSpi
category: java
tags: ['java se', 'javax.security.auth.login', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConfigurationSpi.metodos valor="engineGetAppConfigurationEntry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract AppConfigurationEntry[] engineGetAppConfigurationEntry(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Clase Padre
[ConfigurationSpi](/Java/ConfigurationSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConfigurationSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
