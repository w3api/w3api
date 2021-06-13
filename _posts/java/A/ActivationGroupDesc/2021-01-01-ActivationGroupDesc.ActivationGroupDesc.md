---
title: ActivationGroupDesc.ActivationGroupDesc()
permalink: /Java/ActivationGroupDesc/ActivationGroupDesc/
date: 2021-01-11
key: Java.A.ActivationGroupDesc
category: Java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationGroupDesc.constructores valor="ActivationGroupDesc" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ActivationGroupDesc(String className, String location, MarshalledObject<?> data, Properties overrides, ActivationGroupDesc.CommandEnvironment cmd)
public ActivationGroupDesc(Properties overrides, ActivationGroupDesc.CommandEnvironment cmd)
~~~

## Parámetros
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}
* **String location**,  {% include w3api/param_description.html metodo=_dato parametro="String location" %}
* **Properties overrides**,  {% include w3api/param_description.html metodo=_dato parametro="Properties overrides" %}
* **MarshalledObject&lt;?&gt; data**,  {% include w3api/param_description.html metodo=_dato parametro="MarshalledObject<?> data" %}
* **ActivationGroupDesc.CommandEnvironment cmd**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationGroupDesc.CommandEnvironment cmd" %}

## Clase Padre
[ActivationGroupDesc](/Java/ActivationGroupDesc/)

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
